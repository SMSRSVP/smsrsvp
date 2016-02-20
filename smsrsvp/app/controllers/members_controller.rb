class MembersController < ApplicationController
  def new
    @member = Member.new
  end

  def create
    @member = Member.new(member_params)
    if @member.save
      redirect_to new_member_path
    end
  end

  def member_params
    params.require(:member).permit(:username, :password)
  end
end
